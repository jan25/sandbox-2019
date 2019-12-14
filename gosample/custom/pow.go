package mymath

// Pow is a raised to the bth power
func Pow(a, b int) int {
	p := 1
	for b > 0 {
		p *= a
		b--
	}
	return p
}
