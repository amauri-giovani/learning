import styled from 'styled-components';


export const TodosCSS = styled.div`
  .box {
    height: 150px;
    margin: 18px;
    border: 1px solid black;
    display: flex;
    align-items: center;
    justify-content: space-between;

    &:hover {
      background: #f0f0f5;
    }
  }

  .box button {
    background: #18A0FB;
    font-weight: bold;
    color: #fff;
    width: 97px;
    height: 52px;
    border: 0;
    border-radius: 10px;
    margin-right: 18px;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  .box button:hover {
    background: #1c8dd8;
  }

  .dados-pkmn {
    display: flex;
    align-items: center;
  }

  .dados-pkmn img {
    display: flex;
    margin-left: 18px;
  }

  .dados-pkmn ul {
    list-style: none;
    margin-left: 20px;
  }

  .dados-pkmn ul li {
    margin-top: 10px;
  }

  .dados-pkmn ul li:first-child {
    margin-top: 0;
  }
`;