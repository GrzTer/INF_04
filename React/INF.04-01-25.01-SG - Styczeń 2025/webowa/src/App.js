import "./App.css";
import { useState } from "react";
import 'bootstrap/dist/css/bootstrap.css';

function App() {
  // Stan przechowujący aktywne kategorie
  const [active, setActive] = useState({
    kwiaty: true,
    zwierzeta: true,
    samochody: true,
  });
  
  // Tablica zdjęć
  const DANE = [{id: 0, alt: "Mak", filename: "obraz1.jpg", category:1, downloads: 35},
    {id: 1, alt:"Bukiet", filename: "obraz2.jpg", category: 1, downloads: 43},
    {id: 2, alt:"Dalmatyńczyk", filename: "obraz3.jpg", category:2, downloads: 2},
    {id: 3, alt:"Świnka morska", filename: "obraz4.jpg", category:2, downloads: 53},
    {id: 4, alt:"Rotwailer", filename: "obraz5.jpg", category:2, downloads: 43},
    {id: 5, alt:"Audi", filename: "obraz6.jpg", category:3, downloads: 11},
    {id: 6, alt:"kotki", filename: "obraz7.jpg", category:2, downloads: 22},
    {id: 7, alt:"Róża", filename: "obraz8.jpg", category:1, downloads: 33},
    {id: 8, alt:"Świnka morska", filename: "obraz9.jpg", category:2, downloads: 123},
    {id: 9, alt:"Foksterier", filename: "obraz10.jpg", category:2, downloads: 22},
    {id: 10, alt:"Szczeniak", filename: "obraz11.jpg", category:2, downloads: 12},
    {id: 11, alt:"Garbus", filename: "obraz12.jpg", category:3, downloads: 321}];
    
  const [photos, setPhotos] = useState(DANE);
  // Mapa kategorii
  const catKey = { 1: "kwiaty", 2: "zwierzeta", 3: "samochody" };

  // Filtracja zdjęć według aktywnych kategorii
  const widoczne = photos.filter((foto) => active[catKey[foto.category]]);

  // Funkcja zwiększająca liczbę pobrań
  const incDownloads = id => setPhotos(prev => prev.map(f => f.id === id ? { ...f, downloads: f.downloads + 1 } : f));

  return (
    <div>
      <h1>Kategorie zdjęć</h1>

      {/* Przełączniki do wyboru kategorii */}
      <div className="d-flex flex-row">
        <div className="form-check form-switch">
          <input
            className="form-check-input"
            type="checkbox"
            id="kwiatySwitch"
            checked={active.kwiaty}
            onChange={() =>
              setActive((prev) => ({ ...prev, kwiaty: !prev.kwiaty }))
            }></input>
          <label className="form-check-label" htmlFor="kwiatySwitch">
            Kwiaty
          </label>
        </div>
        <div className="form-check form-switch">
          <input
            className="form-check-input"
            type="checkbox"
            id="zwirzetaSwitch"
            checked={active.zwierzeta}
            onChange={() =>
              setActive((prev) => ({ ...prev, zwierzeta: !prev.zwierzeta }))
            }></input>
          <label className="form-check-label" htmlFor="zwirzetaSwitch">
            Zwierzęta
          </label>
        </div>
        <div className="form-check form-switch">
          <input
            className="form-check-input"
            type="checkbox"
            id="samochodySwitch"
            checked={active.samochody}
            onChange={() =>
              setActive((prev) => ({ ...prev, samochody: !prev.samochody }))
            }></input>
          <label className="form-check-label" htmlFor="samochodySwitch">
            Samochody
          </label>
        </div>
      </div>
      <div className="zdjecia">
        {/* Wyświetlanie zdjęć */}
        {widoczne.map((foto) => (
          <div key={foto.id} className="foto">
            <img src={`/assets/${foto.filename}`} alt={foto.alt} />{" "}
            <h4>Pobrań: {foto.downloads}</h4>
            <button onClick={() => incDownloads(foto.id)}>Pobierz</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
