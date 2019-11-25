import React from 'react';
import { LogScreenStyles } from '../styles/DashBoardStyles';
// import ChatBox from '../molecules/ChatBox';

const LogScreen = ({ logs }) => {
  if (logs.error_msg) {
    return (
      <LogScreenStyles>
        <h1>Room</h1>
        <p>{logs.error_msg}</p>
      </LogScreenStyles>
    );
  }
  return (
    <div>
      <LogScreenStyles>
        <h1>Room</h1>
        <p>Room title: {logs.title}</p>
        <p>Room description: {logs.description}</p>
      </LogScreenStyles>
     
    </div>
  );
};

export default LogScreen;
