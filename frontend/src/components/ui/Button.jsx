const Button = ({ children }) => {
  return (
    <button className="w-full rounded-xl bg-blue-600 py-3 font-semibold text-white shadow-md shadow-blue-300/50 transition hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
      {children}
    </button>
  );
};

export default Button;
