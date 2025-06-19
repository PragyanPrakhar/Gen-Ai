"use client"

import { useState } from "react"
import UploadScreen from "./components/UploadScreen"
import ChatScreen from "./components/ChatScreen"

function App() {
  const [isUploaded, setIsUploaded] = useState(false)
  const [uploadedFileName, setUploadedFileName] = useState("")

  const handleUploadSuccess = (fileName) => {
    setUploadedFileName(fileName)
    setIsUploaded(true)
  }

  const handleBackToUpload = () => {
    setIsUploaded(false)
    setUploadedFileName("")
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {!isUploaded ? (
        <UploadScreen onUploadSuccess={handleUploadSuccess} />
      ) : (
        <ChatScreen fileName={uploadedFileName} onBackToUpload={handleBackToUpload} />
      )}
    </div>
  )
}

export default App
