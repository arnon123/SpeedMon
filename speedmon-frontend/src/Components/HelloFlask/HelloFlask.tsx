import { useState } from 'react';
import './HelloFlask.css';
import { dataService } from '../../Services/DataService';

function HelloFlask(): JSX.Element {
  const [data, setData] = useState<string>('');
  const [name, setName] = useState<string>('');

  const handleHelloClick = async () => {
    try {
      const response = await dataService.getHello();
      setData(JSON.stringify(response));
    } catch (error) {
      console.log(error.message);
    }
  };

  const handleGreetClick = async () => {
    try {
      const response = await dataService.getGreet(name);
      setData(JSON.stringify(response));
    } catch (error) {
      console.log(error.message);
    }
  };

  return (
    <div className="HelloFlask">
      <button
        onClick={() => {
          handleHelloClick();
        }}
      >
        Hello Flask
      </button>
      <p>{data}</p>
      <hr />
      <input
        type="text"
        placeholder="Enter your name"
        onChange={(e) => {
          setName(e.target.value);
        }}
      />
      <button
        onClick={() => {
          handleGreetClick();
        }}
      >
        Greet Flask
      </button>
    </div>
  );
}

export default HelloFlask;
