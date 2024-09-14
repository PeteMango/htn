package main

import (
	"fmt"
	"log"
	"os"

	"github.com/joho/godotenv"
	"github.com/supabase-community/supabase-go"
)

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Fatalf("Error loading .env file")
	}

	API_URL := os.Getenv("API_URL")
	API_KEY := os.Getenv("API_KEY")

	if API_URL == "" || API_KEY == "" {
		log.Fatalf("API_URL or API_KEY not set in environment")
	}

	client, err := supabase.NewClient(API_URL, API_KEY, nil)
	if err != nil {
		fmt.Println("cannot initalize client", err)
	}
	data, count, err := client.From("toilets").Select("*", "exact", false).Execute()
	if err != nil {
		fmt.Println("Error fetching data:", err)
		return
	}

	// data, count, err := client.From("toilets").Select("*", "exact", false).Execute()
	print(data, count)
}
