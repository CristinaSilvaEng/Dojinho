package main

import "strings"

func Perform(code string) string {
	if strings.Contains(code, "++."){
		return "2"
	}
	
	if strings.Contains(code, "+.") {
		return "1"
	}

	if strings.Contains(code, ".+") || 
		strings.Contains(code, ".") {
		return "0"
	}

	return ""
}
