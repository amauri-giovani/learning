import React, { useState, useEffect } from 'react';
import { MeusCSS } from './style.js';
import ImgPKM from '../../images/ImgPKM.svg';


export default function MeusPKMN() {
  const [meusPokemons, setMeusPokemons] = useState(() => {
    const storagedMeusPokemons = localStorage.getItem('@PokeAPI:MeusPKMN');
    if(storagedMeusPokemons) {
      return JSON.parse(storagedMeusPokemons);
    } else {
      return [];
    }
  });

  useEffect(() => {
    localStorage.getItem('@PokeAPI:MeusPKMN');
  }, [meusPokemons]);

  // function capturar() {
  //   setProjects([...projects, `Novo projeto ${Date.now()}`]);
  // }

  return (
    <MeusCSS>
      {meusPokemons.map(pokemon => (
        <div key={pokemon.name} className="box">
          <div className="dados-pkmn">
            <img src={ImgPKM} alt="" />
            <ul>
              <li><h3># NÚMERO POKEMON</h3></li>
              <li><h4>{pokemon.name}</h4></li>
              <li><h5>TIPO (TIPOS)</h5></li>
            </ul>
          </div>
          <button type="submit">Soltar</button>
        </div>
      ))}
    </MeusCSS>
  )
}