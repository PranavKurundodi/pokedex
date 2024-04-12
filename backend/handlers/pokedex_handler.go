package handlers

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os/exec"
	"strings"

	"github.com/PranavKurundodi/pokedex/backend/models"
)

var pokedex []models.Pokemon

func SetPokedex(pd []models.Pokemon) {
	pokedex = pd
}

func GetPokemon(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(pokedex)
}

func GetPokemonByName(w http.ResponseWriter, r *http.Request) {
	queryParams := r.URL.Query()
	name := queryParams.Get("name")

	var foundPokemon *models.Pokemon

	for _, pokemon := range pokedex {
		if pokemon.Name == name {
			foundPokemon = &models.Pokemon{
				Name:      pokemon.Name,
				Type1:     pokemon.Type1,
				Type2:     pokemon.Type2,
				Evolution: pokemon.Evolution,
			}

			break
		}
	}

	if foundPokemon == nil {
		http.NotFound(w, r)
		return
	}

	json.NewEncoder(w).Encode(foundPokemon)
}

func PokemonProbModel(w http.ResponseWriter, r *http.Request) {
	cmd := exec.Command("python", "C:\\Users\\prana\\OneDrive\\Documents\\college\\pokedex\\backend\\model\\test.py")

	// Create a buffer to store the output
	var stdout, stderr bytes.Buffer
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr

	// Run the command and wait for it to finish
	err := cmd.Run()
	if err != nil {
		log.Fatalf("Failed to run Python script: %v\nStderr: %s", err, stderr.String())
	}

	// Get the output of the Python script
	pythonOutput := stdout.String()

	// Use the Python output as needed in your Go code
	parts := strings.Split(pythonOutput, "] ")
	pokemonPart := strings.Trim(parts[0], "[]")
	probPart := strings.Trim(parts[1], "[]")

	// Split Pokémon names and probabilities into arrays
	top3pokemons := strings.Split(pokemonPart, ", ")
	probabilitiesStr := strings.Split(probPart, ", ")

	// Convert probabilities from string to float64
	var top3prob []float64
	for _, str := range probabilitiesStr {
		var prob float64
		_, err := fmt.Sscanf(str, "%f", &prob)
		if err != nil {
			panic(err)
		}
		top3prob = append(top3prob, prob)
	}

	type ModelResult struct {
		Pokemon     string
		Probability float64
	}
	var modelResults []ModelResult

	// Iterate over the arrays and store each result as a ModelResult struct
	for i := 0; i < len(top3pokemons); i++ {
		result := ModelResult{
			Pokemon:     top3pokemons[i],
			Probability: top3prob[i],
		}
		modelResults = append(modelResults, result)
	}
	json.NewEncoder(w).Encode(modelResults)

}
