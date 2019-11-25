import axios from "axios";

/**
 * Creates a config object with commonly used URLs or keys throughout the application
 * Allows for single spot updating of frequently used information across components
 * axiosWithAuth returns an axios instance with the authorization headers and baseURL
 */

const config = {
  baseUrl: `https://lambda-treasure-hunt.herokuapp.com/api/adv`,

  /**
   * @returns an Authorization Header with the user's authToken
   */
  
  axiosWithAuth: function(){
      return axios.create({
          baseURL: this.baseUrl,
          headers: {
              Authorization: `Token ${localStorage.getItem('key')}`
          }
      });
  }
};

export default config;
