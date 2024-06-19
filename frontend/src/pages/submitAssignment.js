import React, { useState } from "react";
import axios from "axios";
import { Typography, Box, Button, Container, Paper, CircularProgress } from "@mui/material";
import {
  faCloudArrowDown,
  faFolderOpen,
  faPenToSquare,
  faComment,
} from "@fortawesome/free-solid-svg-icons";
import UploadButton from "../components/UploadButton";
import Chat from "../pages/chat"; // Import your Chat component
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const serviceList = [
  {
    title: "STEP 1: Upload Assignment",
    icon: faFolderOpen,
    description:
      "Submit your handwritten assignment and our system will read your handwritten image to generate an text for it.",
  },
  {
    title: "STEP 2: Get Answer by AI",
    icon: faComment,
    description:
      "The next step allows you to modify our generated text and get a response using AI.",
  },
  {
    title: "STEP 3: Get Paraphrased and Handwritten",
    icon: faPenToSquare,
    description:
      "Get your answers paraphrased for eliminating plagiarism and get a handwritten copy.",
  },
];

function CreatePost() {
  const [content, setContent] = useState("");
  const [file, setFile] = useState(null);
  const [isChatEnabled, setIsChatEnabled] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const ocrApi = process.env.REACT_APP_API + "/ocr";
  console.log("ocrApi", ocrApi);

  const handleFileSelect = (selectedFile) => {
    const allowedTypes = ["application/pdf", "image/jpeg", "image/png"];
    if (allowedTypes.includes(selectedFile.type)) {
      setFile(selectedFile);
    } else {
      alert("Please upload a valid PDF or image file.");
    }
  };

  const handlePostClick = async () => {
    try {
      if (!file) {
        console.log("No file selected");
        return;
      }

      setIsLoading(true); // Start loader

      const formData = new FormData();
      formData.append("file", file);

      const uploadResponse = await axios.post(ocrApi, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setContent(uploadResponse.data);
      console.log("Files uploaded successfully:", uploadResponse.data);
      setIsChatEnabled(true);
      return uploadResponse.data;
    } catch (error) {
      console.error("Failed to upload file!", error);
    } finally {
      setIsLoading(false); // Stop loader
    }
  };

  return (
    <Box sx={{ bgcolor: "#C1C8E4", width: "100vw", height: "100vh" }}>
      <Container sx={{ pt: "30px" }}>
        <Typography
          sx={{
            color: "#fff",
            fontSize: "35px",
            fontStyle: "normal",
            fontWeight: "800",
            lineHeight: "normal",
          }}
        >
          Assignment Solver by Ali Hassan and Nashit Budhwani
        </Typography>
        <Box
          sx={{
            pt: 4,
            display: "flex",
            flexDirection: "row",
            justifyContent: "space-between",
            gap: 4,
          }}
        >
          {serviceList.map((service, index) => (
            <Paper
              key={index}
              elevation={3}
              sx={{ height: "230px", width: "400px", bgcolor: "#8860D0" }}
            >
              <Box sx={{ mt: 3, ml: "20px" }}>
                <Typography color="primary" sx={{ fontWeight: "600" }}>
                  {service.title}
                </Typography>
                <Box sx={{ my: 2, mx: "120px" }}>
                  <FontAwesomeIcon
                    icon={service.icon}
                    style={{ fontSize: "60px", color: "#C1C8E4" }}
                  />
                </Box>
                <Typography color="primary" sx={{ fontWeight: 400 }}>
                  {service.description}
                </Typography>
              </Box>
            </Paper>
          ))}
        </Box>
        <Box
          sx={{
            ml: 0,
            mt: 6,
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          {isChatEnabled ? (
            <Chat answer={content} />
          ) : (
            <UploadButton icon={faCloudArrowDown} onFileSelect={handleFileSelect} />
          )}
          {!isChatEnabled && (
            <Button
              variant="contained"
              color="tertiary"
              onClick={handlePostClick}
              sx={{
                color: "#fff",
                width: "360px",
                "&:hover": {
                  bgcolor: "#8860D0",
                },
              }}
              disabled={isLoading} // Disable button when loading
            >
              {isLoading ? <CircularProgress size={24} color="inherit" /> : "Submit"}
            </Button>
          )}
        </Box>
      </Container>
    </Box>
  );
}

export default CreatePost;
