const InputField = ({ label, type, placeholder }) => {
  return (
    <div>
      <label className="text-sm font-semibold text-[#1f3556]">{label}</label>
      <div className="relative mt-2">
        <input
          type={type}
          placeholder={placeholder}
          className="w-full rounded-xl border border-[#b8c5d8] bg-white px-4 py-3 text-gray-800 placeholder-gray-400 transition focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        {type === "password" && (
          <span className="pointer-events-none absolute inset-y-0 right-4 flex items-center text-[#8aa0bf]">
            <svg viewBox="0 0 24 24" fill="none" className="h-5 w-5" stroke="currentColor" strokeWidth="2">
              <path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6Z" />
              <circle cx="12" cy="12" r="3" />
            </svg>
          </span>
        )}
      </div>
    </div>
  );
};

export default InputField;
