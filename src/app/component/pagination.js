// components/Pagination.js
export default function Pagination({ currentPage, totalPages, onPageChange }) {
  return (
    <div className="mt-6 flex justify-center space-x-2">
      {Array.from({ length: totalPages }, (_, i) => i + 1).map((num) => (
        <button
          key={num}
          onClick={() => onPageChange(num)}
          className={`px-4 py-2 rounded ${
            currentPage === num
              ? "bg-teal-500 text-white"
              : "bg-gray-700 text-gray-300 hover:bg-gray-600"
          }`}
        >
          {num}
        </button>
      ))}
    </div>
  );
}
