import styled from 'styled-components';
import Lupa from '../../images/Search.svg';


export const HeaderCSS = styled.header`
  .header {
    height: 108px;
    margin: 18px;
    border: 1px solid black;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .logo {
    display: flex;
    margin-left: 18px;
  }

  .menu-search ul {
    display: flex;
    align-items: center;
    margin-right: 18px;
  }

  .menu-search ul li, input {
    list-style: none;
    margin-left: 20px;
  }
  
  .menu-search ul input {
    /* background: url(${Lupa}) no-repeat right;
    background-size: 7%;
    background-position-x: 98%; */
    border: 1px solid black;

    border-radius: 5px 0 0 5px;
    border-right: none;
    width: 18vw;
    height: 26px;
    padding: 0 10px 0 5px;
  }

  a:hover {
      opacity: 1;
    }

  .menu-search ul form {
      display: flex;
    }

  .menu-search ul form button {
    background: #FFF url(${Lupa}) no-repeat center;
    background-size: 70%;
    /* background-position-x: -200%; */
    /* border: 11px solid; */
      
    width: 2vw;
    /* padding: 25px; */
    /* border: 0; */
    cursor: pointer;
    height: 26px;
    border: 1px solid black;

    border-radius: 0 5px 5px 0;
    border-left: none;
  }
`;
