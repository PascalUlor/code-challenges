import React, { useState, useEffect } from 'react';
import Pusher from 'pusher-js';
import DashBoard from '../~reuseables/molecules/DashBooard';
import config from '../../axios';

const { REACT_APP_PUSHER_API_KEY } = process.env;
const GameArea = () => {
  const [gameData, setGameData] = useState([]);
  const [rooms, setRooms] = useState([]);
  const [currentRoom, setCurrentRoom] = useState({});
  const [message, setMessage] = useState('');

  /**
   * Initialze Pusher
   */
  const pusher = new Pusher(REACT_APP_PUSHER_API_KEY, {
    cluster: 'eu',
    forceTLS: true
  });

  const sendMessage = message => {
    config
      .axiosWithAuth()
      .post(`/api/say`, { message })
      .then(res => {
        setMessage(message);
      })
      .catch(err => {
        return err.statusText;
      });
  };

  const subscriber = uuid => {
    const channel = pusher.subscribe(`p-channel-${uuid}`);
    channel.bind('broadcast', function(data) {
      console.log(JSON.stringify(data));
    });
  };
  /**
   * Initializes game and users,
   *@param: none
   */
  const LoadGame = () => {
    config
      .axiosWithAuth()
      .get(`/api/init`)
      .then(res => {
        setGameData(res.data);
      })
      .catch(err => {
        return err.statusText;
      });
  };

  async function LoadRooms() {
    await config
      .axiosWithAuth()
      .get(`/api/rooms/`)
      .then(res => {
        setRooms(res.data);
      })
      .catch(err => {
        return err.statusText;
      });
  }

  const actionDirection = direction => {
    config
      .axiosWithAuth()
      .post(`/api/move`, { direction })
      .then(res => {
        // console.log(res.data)
        setCurrentRoom(res.data);
        setGameData(res.data);
      })
      .catch(err => {
        return err.statusText;
      });
  };

  useEffect(() => {
    LoadGame();
    LoadRooms();
  }, []);
  return (
    <DashBoard
      data={gameData}
      location={currentRoom}
      rooms={rooms}
      action={actionDirection}
      speak={sendMessage}
      subscriber={subscriber}
      chat={message}
    />
  );
};

export default GameArea;
