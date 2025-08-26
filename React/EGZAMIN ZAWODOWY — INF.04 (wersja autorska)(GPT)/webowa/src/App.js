import "bootstrap/dist/css/bootstrap.css";
import React, { useMemo, useState } from "react";

const CAT_LABELS = { 1: "Frontend", 2: "Backend", 3: "DevOps" };

const initialCourses = [
  {
    id: 1,
    title: "React od podstaw",
    category: 1,
    level: "Beginner",
    enrolled: 42,
    filename: "react.png",
  },
  {
    id: 2,
    title: "Nowoczesny CSS i Flex/Grid",
    category: 1,
    level: "Intermediate",
    enrolled: 27,
  },
  {
    id: 3,
    title: "Node.js API z Express",
    category: 2,
    level: "Intermediate",
    enrolled: 55,
  },
  {
    id: 4,
    title: "SQL i projektowanie baz",
    category: 2,
    level: "Beginner",
    enrolled: 31,
  },
  {
    id: 5,
    title: "Docker w praktyce",
    category: 3,
    level: "Beginner",
    enrolled: 73,
    filename: "docker.png",
  },
  {
    id: 6,
    title: "Kubernetes podstawy",
    category: 3,
    level: "Advanced",
    enrolled: 18,
  },
  {
    id: 7,
    title: "TypeScript dla React",
    category: 1,
    level: "Advanced",
    enrolled: 12,
  },
  {
    id: 8,
    title: "NestJS – architektura",
    category: 2,
    level: "Advanced",
    enrolled: 9,
  },
];

export default function App() {
  const [courses, setCourses] = useState(initialCourses);
  const [filters, setFilters] = useState({ 1: true, 2: true, 3: true }); // domyślnie wszystko włączone

  const toggleFilter = (cat) => {
    setFilters((prev) => ({ ...prev, [cat]: !prev[cat] }));
  };

  const handleEnroll = (id) => {
    setCourses((prev) =>
      prev.map((c) => (c.id === id ? { ...c, enrolled: c.enrolled + 1 } : c))
    );
  };

  const visibleCourses = useMemo(
    () => courses.filter((c) => filters[c.category]),
    [courses, filters]
  );

  return (
    <div className="container py-4">
      <h1 className="mb-4">Katalog kursów</h1>

      {/* Przełączniki filtrów */}
      <div className="mb-4">
        {[1, 2, 3].map((cat) => (
          <div key={cat} className="form-check form-switch form-check-inline">
            <input
              className="form-check-input"
              type="checkbox"
              id={`switch-${cat}`}
              checked={!!filters[cat]}
              onChange={() => toggleFilter(cat)}
            />
            <label className="form-check-label" htmlFor={`switch-${cat}`}>
              {CAT_LABELS[cat]}
            </label>
          </div>
        ))}
      </div>

      {/* Siatka kart */}
      <div className="row g-3">
        {visibleCourses.length === 0 && (
          <div className="col-12">
            <div className="alert alert-secondary mb-0">
              Brak kursów dla wybranych filtrów.
            </div>
          </div>
        )}

        {visibleCourses.map((course) => (
          <div key={course.id} className="col-12 col-md-6 col-lg-4">
            <div className="card h-100 shadow-sm rounded-3">
              {course.filename && (
                <img
                  src={`/assets/${course.filename}`}
                  className="card-img-top"
                  alt={course.title}
                  style={{ objectFit: "cover", height: 160 }}
                />
              )}
              <div className="card-body d-flex flex-column">
                <h5 className="card-title mb-1">{course.title}</h5>
                <h6 className="card-subtitle text-muted mb-2">
                  Poziom: {course.level} • {CAT_LABELS[course.category]}
                </h6>
                <p className="card-text mb-3">
                  Zapisanych: <strong>{course.enrolled}</strong>
                </p>
                <div className="mt-auto">
                  <button
                    className="btn btn-success w-100"
                    onClick={() => handleEnroll(course.id)}
                  >
                    Zapisz się
                  </button>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Stopka (opcjonalnie) */}
      <div className="text-muted small mt-4">
        <span className="me-2">Widok responsywny (2–3 karty w rzędzie).</span>
        <span>Przełączniki sterują filtrem po kategoriach.</span>
      </div>
    </div>
  );
}
