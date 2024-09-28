package main

import (
	"fmt"
	"gopkg.in/yaml.v3"
	"io"
	"os"
)

type SongCategories struct {
	FemaleVocal     []string `yaml:"female_vocal"`
	MaleVocal       []string `yaml:"male_vocal"`
	FastPaced       []string `yaml:"fast_paced"`
	MediumSlow      []string `yaml:"medium_slow"`
	StronglyEmotive []string `yaml:"strongly_emotive"`
	English         []string `yaml:"english"`
}

func read(filename string) string {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}

	defer file.Close()
	b, err := io.ReadAll(file)
	return string(b)
}

func parse(raw_data string) SongCategories {
	SongData := SongCategories{}
	err := yaml.Unmarshal([]byte(raw_data), &SongData)
	if err != nil {
		panic(err)
	}

	return SongData
}

func main() {
	fmt.Println("Hello World")

	raw_data := read("../data.yaml")

	SongData := parse(raw_data)

	fmt.Printf("SongData :\n%v\n\n", SongData)

}
