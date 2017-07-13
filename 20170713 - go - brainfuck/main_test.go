package main

import "testing"

type testcase struct {
	input string
	expect string
}

var tests = []testcase{
	{"", ""},
	{".", "0"},
	{"+.", "1"},
	{".+", "0"},
	{"-", ""},
	{"++.", "2"},
}

func TestPerform(t *testing.T) {
	for _, pair := range tests {
		actual := Perform(pair.input)
		if actual != pair.expect {
			t.Error(
				"For", pair.input,
				"expected", pair.expect,
				"got", actual,
			)
		}
	}
}
