import ReactDOM from 'react-dom/client';
import Counter from './Components/Counter/Counter';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(<Counter />);
