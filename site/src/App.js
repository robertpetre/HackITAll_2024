import Header from './Components/Header';
import Companies from './Components/Companies';
import './app.css';

function App() {
  return (
    <div className="h-screen flex flex-col">
      {/* Header takes 50% of the screen height on large screens, full height on small screens */}
      <div className="lg:h-4/5 h-full">
        <Header />
      </div>

      {/* Companies take 50% of the screen height on large screens, full height on small screens */}
      <div className="lg:h-1/5 h-fit">
        <Companies />
      </div>
    </div>
  );
}

export default App;
