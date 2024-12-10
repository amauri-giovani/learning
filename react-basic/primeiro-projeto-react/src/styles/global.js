import { createGlobalStyle } from 'styled-components';


export default createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    outline: 0;
    box-sizing: border-box;
  }

  body {
    /* background: #f0f0f5; */
    background: #fff;
    -webkit-font-smoothing: antialiased;
  }

  body, input, button {
    font: 16px Roboto, sans-serif;
  }

  a {
    text-decoration: none;
    font-weight: bold;
    color: #000;
    opacity: 0.6;
  }

`