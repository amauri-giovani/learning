import React, { useEffect, useState } from 'react';
import ImgLogo from '../../images/ImgLogo.svg';
import { HeaderCSS } from './style.js';


export default function Header() {
  const [busca, setBusca] = useState('');

function InputUSer(event){
  event.preventDefault();
  // console.log(busca);
  
    setBusca('');
  }

  return (
    <HeaderCSS>
      <div className="header">
        <div className="logo">
          <img src={ImgLogo} alt="Logo" />
        </div>
        <div className="menu-search">
          <ul>
            <li><a href="">Todos PKMN</a></li>
            <li><a href="">Meus PKMN</a></li>
            <form action="." onSubmit={InputUSer}>
              <input value={busca} onChange={(e) => setBusca(e.target.value)} type="text" placeholder="Search" />
              <button type="submit"></button>
            </form>
          </ul>
        </div>
      </div>
    </HeaderCSS>
  );
}