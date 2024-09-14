package main

import (
	"fmt"

	"github.com/supabase-community/supabase-go"
)

func main() {
	client, err := supabase.NewClient(API_URL, API_KEY, "", nil)
	if err != nil {
		fmt.Println("cannot initalize client", err)
	}
	data, count, err := client.From("countries").Select("*", "exact", false).Execute()

}
