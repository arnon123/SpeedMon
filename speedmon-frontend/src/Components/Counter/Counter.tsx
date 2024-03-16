import { useState } from 'react';
import './Counter.css';

function Counter(): JSX.Element {
  const [count, setCount] = useState(0);

  return (
    <div className="Counter">
      <p>Counter: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
    </div>
  );
}

export default Counter;
