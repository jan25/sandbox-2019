package main

import (
	"fmt"
	"reflect"

	"github.com/ghodss/yaml"
)

type Values map[string]interface{}

func main() {
	vals := make(Values)
	vals["Image"] = Values{"Tag": 20190612073634}

	b, _ := yaml.Marshal(vals)
	y := string(b)
	fmt.Printf("After Marshal:\n %v", y)

	yaml.Unmarshal(b, &vals)

	fmt.Printf("After UnMarshal:\n %v", vals)
	b, _ = yaml.Marshal(vals)
	y = string(b)
	fmt.Printf("After Marshal:\n %v", y)

	tag, _ := vals["Image"].(map[string]interface{})["Tag"]
	fmt.Print(reflect.TypeOf(tag))
}
