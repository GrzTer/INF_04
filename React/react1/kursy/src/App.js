import './App.css';

function App() {
  const data_jakas = ["jeden", "dwa", "trzy"]
  const handleSubmit = (event) =>
  {
    event.preventDefault();
    const form = event.target();

    const userName = form.elements["user-name"].value;
    const userCourses = form.elements["user-course"].value;
  }
  return (
    <div>
    <h1>Liczba kursów: {data_jakas.length}</h1>
    <ol>
    {
      data_jakas.map((dat) => {
        <li>{dat}</li>
      })
    }
    </ol>
    <form onSubmit={handleSubmit}>
      <label for="user-name">Imię i nazwisko:</label>
      <input name='user-name' type='tekst'/><br/>
      <label for="user-course">Numer kursu:</label>
      <input name='user-course' type='tekst'/><br/>
      <button type='submit'>Zapisz do kusu</button>
    </form>
    </div>
  );
}

export default App;
