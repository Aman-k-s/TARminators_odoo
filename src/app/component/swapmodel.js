export default function SwapModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-70 flex justify-center items-center z-50">
      <div className="bg-gray-800 p-6 rounded-lg w-full max-w-md shadow-xl">
        <h2 className="text-lg font-semibold mb-4">Request a Swap</h2>
        {/* Skill inputs here */}
        <div className="flex justify-end gap-2">
          <button onClick={onClose} className="px-4 py-2 rounded bg-gray-600 hover:bg-gray-700">
            Cancel
          </button>
          <button className="px-4 py-2 rounded bg-teal-500 hover:bg-teal-600">Submit</button>
        </div>
      </div>
    </div>
  );
}
