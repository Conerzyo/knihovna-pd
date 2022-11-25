import Link from "next/link";

export default function Home() {
  return (
    <div style={containerStyles}>
      <div>Knihovna PD</div>
      <div style={innerHeader}>
        <div>Logged user</div>
        <Link href="/login">Login</Link>
      </div>
    </div>
  );
}

const containerStyles = {
  display: "flex",
  justifyContent: "space-between",
  padding: "8px 12px",
};

const innerHeader = {
  display: "flex",
};
