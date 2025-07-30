import { useState } from "react";

export default function CourseSignup() {
  const [courses] = useState([
    "Programowanie w C#",
    "Angular dla początkujących",
    "Kurs Django",
  ]);

//   handleSubmit

  return (
    <div className="container mt-4">
      <h2>Liczba kursów: {courses.length}</h2>
      <ol>
        {courses.map((course, idx) => (
          <li key={idx}>{course}</li>
        ))}
      </ol>
      <form>
        <label htmlFor="name_surname">Imię i nazwisko:</label>
        <input
          type="text"
          name="name_surname"
          id="name_surname"
          className="form-control "
        />
        <label htmlFor="courseNr">Numer kursu:</label>
        <input
          type="number"
          name="courseNr"
          id="courseNr"
          className="form-control"
        />
        <button type="submit" className="btn btn-primary">
          Zapisz do kursu
        </button>
      </form>
    </div>
  );
}
