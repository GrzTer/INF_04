/*
Lokalizacja: app/src/Form.js:
*/

/******************************************************
 nazwa klasy: FilmForm
 pola: formData - obiekt przechowujący dane formularza
 metody: handleChange, void – obsługuje zmiany w polach formularza
         handleSubmit, void – obsługuje zdarzenie przesłania formularza
 informacje: Komponent reprezentuje formularz dodawania filmów z polami 
             tytułu oraz kategorii filmu. Dane są wyświetlane w konsoli.
 autor: Grzegorz Tereszkiewicz
*****************************************************/

import React, { useState } from "react";

const FilmForm = () => {
  const [formData, setFormData] = useState({
    title: "",
    genre: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(`tytul: ${formData.title}; rodzaj: ${formData.genre}`);
  };

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Formularz filmu</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="title" className="form-label">
            Tytuł filmu
          </label>
          <input
            type="text"
            className="form-control"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="genre" className="form-label">
            Rodzaj
          </label>
          <select
            className="form-select"
            id="genre"
            name="genre"
            value={formData.genre}
            onChange={handleChange}>
            <option value="">Wybierz...</option>
            <option value="1">Komedia</option>
            <option value="2">Obyczajowy</option>
            <option value="3">Sensacyjny</option>
            <option value="4">Horror</option>
          </select>
        </div>
        <button type="submit" className="btn btn-primary">
          Dodaj
        </button>
      </form>
    </div>
  );
};

export default FilmForm;
