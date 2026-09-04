import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import About from "./components/About";
import Projects from "./components/Projects";
import ChatWindow from "./components/chat/ChatWindow";
import Contact from "./components/Contact";
import Footer from "./components/Footer";

function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <Navbar />

      <main>
        <Hero />
        <About />
        <Projects />
        <ChatWindow />
        <Contact />
      </main>

      <Footer />
    </div>
  );
}

export default App;