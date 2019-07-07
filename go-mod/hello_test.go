package hello

import (
	"fmt"
	"testing"
)

func TestHello(t *testing.T) {
	want := "Hello, world."
	fmt.Println(Hello())
	if got := Hello(); got != want {
		t.Errorf("Hello() = %q, want %q", got, want)
	}
}
