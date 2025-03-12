import { useState, useEffect } from "react";
import { motion } from "framer-motion";

const magnetars = [
  "Magnetar 1",
  "Magnetar 2",
  "Magnetar 3",
  // Add all 30 magnetars here
];

export default function MagnetarDisplay() {
  const [showWelcome, setShowWelcome] = useState(true);

  useEffect(() => {
    // Hide "Welcome" after 3 seconds
    const timer = setTimeout(() => setShowWelcome(false), 3000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="flex justify-center items-center min-h-screen bg-black text-white">
      {showWelcome ? (
        <motion.h1
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 2 }}
          className="text-4xl"
        >
          Welcome
        </motion.h1>
      ) : (
        <motion.div
          className="grid grid-cols-5 gap-4 p-5"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 2 }}
        >
          {magnetars.map((magnetar, index) => (
            <motion.div
              key={index}
              className="p-4 border rounded-lg bg-gray-800 text-center"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              {magnetar}
            </motion.div>
          ))}
        </motion.div>
      )}
    </div>
  );
}
