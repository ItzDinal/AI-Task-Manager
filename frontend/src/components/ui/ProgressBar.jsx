const ProgressBar = ({ label, value }) => {
  return (
    <div>
      <div className="mb-2 flex justify-between text-sm font-medium text-[#5f6f86]">
        <span>{label}</span>
        <span>{value}%</span>
      </div>

      <div className="h-2.5 w-full rounded-full bg-[#d5dbe6]">
        <div
          className="h-2.5 rounded-full bg-gradient-to-r from-blue-500 to-cyan-500"
          style={{ width: `${value}%` }}
        />
      </div>
    </div>
  );
};

export default ProgressBar;
