import { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

const DANE_ZDJEC = [
  { id: 0, alt: "Mak", filename: "obraz1.jpg", category: 1, downloads: 35 },
  { id: 1, alt: "Bukiet", filename: "obraz2.jpg", category: 1, downloads: 43 },
  {
    id: 2,
    alt: "Dalmatyńczyk",
    filename: "obraz3.jpg",
    category: 2,
    downloads: 2,
  },
  {
    id: 3,
    alt: "Świnka morska",
    filename: "obraz4.jpg",
    category: 2,
    downloads: 53,
  },
  {
    id: 4,
    alt: "Rotwailer",
    filename: "obraz5.jpg",
    category: 2,
    downloads: 43,
  },
  { id: 5, alt: "Audi", filename: "obraz6.jpg", category: 3, downloads: 11 },
  { id: 6, alt: "kotki", filename: "obraz7.jpg", category: 2, downloads: 22 },
  { id: 7, alt: "Róża", filename: "obraz8.jpg", category: 1, downloads: 33 },
  {
    id: 8,
    alt: "Świnka morska",
    filename: "obraz9.jpg",
    category: 2,
    downloads: 123,
  },
  {
    id: 9,
    alt: "Foksterier",
    filename: "obraz10.jpg",
    category: 2,
    downloads: 22,
  },
  {
    id: 10,
    alt: "Szczeniak",
    filename: "obraz11.jpg",
    category: 2,
    downloads: 12,
  },
  {
    id: 11,
    alt: "Garbus",
    filename: "obraz12.jpg",
    category: 3,
    downloads: 321,
  },
];
function App() {
  const [listaZdjec, ustawListeZdjec] = useState(DANE_ZDJEC);
  const [widocznoscKategorii, ustawWidocznoscKategorii] = useState({
    kwiaty: true,
    zwierzeta: true,
    samochody: true,
  });
  const zmienWidocznosc = (kategoria) => {
    ustawWidocznoscKategorii((poprzedniStan) => ({
      ...poprzedniStan,
      [kategoria]: !poprzedniStan[kategoria],
    }));
  };
  const pobierzZdjecie = (idWybranegoZdjecia) => {
    const zaktualizowanaLista = listaZdjec.map((zdjecie) => {
      if (zdjecie.id === idWybranegoZdjecia) {
        return { ...zdjecie, downloads: zdjecie.downloads + 1 };
      }
      return zdjecie;
    });
    ustawListeZdjec(zaktualizowanaLista);
  };
  return (
    <div className="container mt-3">
      <h1>Kategorie zdjęć</h1>
      <div className="mb-4">
        <div className="form-check form-switch form-check-inline">
          <input
            className="form-check-input"
            type="checkbox"
            id="switchKwiaty"
            checked={widocznoscKategorii.kwiaty}
            onChange={() => zmienWidocznosc("kwiaty")}
          />
          <label className="form-check-label" htmlFor="switchKwiaty">
            Kwiaty
          </label>
        </div>
        <div className="form-check form-switch form-check-inline">
          <input
            className="form-check-input"
            type="checkbox"
            id="switchZwierzeta"
            checked={widocznoscKategorii.zwierzeta}
            onChange={() => zmienWidocznosc("zwierzeta")}
          />
          <label className="form-check-label" htmlFor="switchZwierzeta">
            Zwierzęta
          </label>
        </div>
        <div className="form-check form-switch form-check-inline">
          <input
            className="form-check-input"
            type="checkbox"
            id="switchSamochody"
            checked={widocznoscKategorii.samochody}
            onChange={() => zmienWidocznosc("samochody")}
          />
          <label className="form-check-label" htmlFor="switchSamochody">
            Samochody
          </label>
        </div>
      </div>
      <div className="row">
        {listaZdjec.map((zdjecie) => {
          if (zdjecie.category === 1 && !widocznoscKategorii.kwiaty)
            return null;
          if (zdjecie.category === 2 && !widocznoscKategorii.zwierzeta)
            return null;
          if (zdjecie.category === 3 && !widocznoscKategorii.samochody)
            return null;

          return (
            <div key={zdjecie.id} className="col-md-4 mb-3">
              <div className="p-2 border rounded">
                <img
                  src={`/assets/${zdjecie.filename}`}
                  alt={zdjecie.alt}
                  className="img-fluid rounded m-1"
                  style={{ margin: "5px" }}
                />
                <h4>Pobrań: {zdjecie.downloads}</h4>
                <button
                  className="btn btn-success"
                  onClick={() => pobierzZdjecie(zdjecie.id)}>
                  Pobierz
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default App;
