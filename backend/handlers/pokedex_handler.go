package handlers

import (
	"encoding/json"
	"net/http"

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
