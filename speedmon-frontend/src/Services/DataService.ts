import axios from 'axios';
import { appConfig } from '../Utils/AppConfig';

class DataService {
  public async getHello(): Promise<JSON> {
    const response = await axios.get(appConfig.helloUrl);
    return response.data;
  }

  public async getGreet(name: string): Promise<JSON> {
    const response = await axios.get(appConfig.greetUrl + name);
    return response.data;
  }
}

export const dataService = new DataService();
