import React from 'react';
import {
  MainContainer,
  Container,
  ControllArea
} from '../styles/DashBoardStyles';
import GameScreen from '../atoms/GameScreen';
import ActionArea from './ActionsArea';
import ChatScreen from '../atoms/ChatScreen';

const DashBoard = ({ data, rooms, action, location, chat, speak, subscriber }) => {
  subscriber(data.uuid);
  return (
    <MainContainer>
      <Container>
        <ControllArea>
          <GameScreen map={rooms} location={location} />
          <ActionArea logs={data} move={action} />
        </ControllArea>
        <ChatScreen chats={chat} sendMessage={speak}/>
      </Container>
    </MainContainer>
  );
};

export default DashBoard;
