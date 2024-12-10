import React, { useState, useEffect } from 'react';
import api from '../../services/api';
import { TodosCSS } from './style.js';
import ImgPKM from '../../images/ImgPKM.svg';


export default function TodosPKM() {
  const [todosPokemons, setTodosPokemons] = useState([]);
  const [meusPokemons, setMeusPokemons] = useState([]);
  // ['Pikachu', 'Magneton', 'Charmander']
  
  useEffect(() => {
    api.get('ability/?limit=5&offset=20').then(response => {
      setTodosPokemons(response.data.results);
    })
  }, []);

  useEffect(() => {
    localStorage.setItem('@PokeAPI:TodosPKMN', JSON.stringify(todosPokemons));
    localStorage.setItem('@PokeAPI:MeusPKMN', JSON.stringify(meusPokemons));
  }, [todosPokemons, meusPokemons]);

  function Capturar(indice) {
    const capturado = todosPokemons.splice(indice, 1);
    setTodosPokemons([...todosPokemons]);
    setMeusPokemons([...meusPokemons, capturado[0]]);
  }

  return (
    <TodosCSS>
      {todosPokemons.map(pokemon => (
        <div key={pokemon.name} className="box">
          <div className="dados-pkmn">
            <img src={ImgPKM} alt="" />
            <ul>
              <li><h3># NÚMERO POKEMON</h3></li>
              <li><h4>{pokemon.name}</h4></li>
              <li><h5>TIPO (TIPOS)</h5></li>
            </ul>
          </div>
          <button type="submit" onClick={(e) => Capturar(todosPokemons.indexOf(pokemon))}>Capturar</button>
        </div>
      ))}
    </TodosCSS>
  )
}