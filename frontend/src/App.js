const sendData = async () => {
  const response = await fetch('http://127.0.0.1:5000/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: 'I am happy' })
  });
  const data = await response.json();
  console.log(data);
};

export default function App() {
  return (
    <div>
      <button onClick={sendData}>Send Data</button>
    </div>
  );
}
