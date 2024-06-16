import React, { useState } from "react";
import axios from "axios";
import {
  Typography,
  Box,
  Button,
  TextField,
  Paper,
  Container,
} from "@mui/material";

function Chat({ answer }) {
  const [content, setContent] = useState(answer.text || "");
  const [gptAnswer, setGptAnswer] = useState("");
  const [paraphrasedAnswer, setParaphrasedAnswer] = useState("");
  const [handwrittenAnswer, setHandwrittenAnswer] = useState("");
  const [isAnswerEnabled, setIsAnswerEnabled] = useState(false);
  const [isParaphraserEnabled, setIsParaphraserEnabled] = useState(false);
  

  const chatApi = process.env.REACT_APP_API + "/gpt";
  const pharaphraseApi = process.env.REACT_APP_API + "/paraphrase";
  const handwrittenApi = process.env.REACT_APP_API + "/handwriting";
  const handleChatClick = async () => {
    try {
      const uploadResponse = await axios.post(
        chatApi,
        {
          user_message: content,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      console.log("Message sent successfully:", uploadResponse.data);
      setGptAnswer(uploadResponse.data.answer);
      setIsAnswerEnabled(true);
      return uploadResponse.data;
    } catch (error) {
      alert("Response timed out please try again!");
      console.error("Failed to send message!", error);
    }
  };

  const handlePharaphaseClick = async () => {
    try {
      const uploadResponse = await axios.post(
        pharaphraseApi,
        {
          input_text: gptAnswer,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      console.log("Message sent successfully:", uploadResponse.data);
      setParaphrasedAnswer(uploadResponse.data.paraphrased_text);
      return uploadResponse.data;
    } catch (error) {
      alert("Response timed out please try again!");
      console.error("Failed to send message!", error);
    }
  };

  const handlehandwrittenClick = async () => {
    try {
      const uploadResponse = await axios.post(
        handwrittenApi,
        {
          text: paraphrasedAnswer,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      console.log("Message sent successfully:", uploadResponse.data);
      setHandwrittenAnswer(uploadResponse.data.handwritten_text);
      return uploadResponse.data;
    } catch (error) {
      alert("Response timed out please try again!");
      console.error("Failed to send message!", error);
    }
  };

  return (
    <Box>
      <Container
        sx={{
          ml: -3,
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
          gap: 4.5,
        }}
      >
        <Box
          sx={{
            width: "370px",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
            gap: 2,
          }}
        >
          <Paper>
            <TextField
              label="Extracted Text From Image"
              color="tertiary"
              fullWidth
              multiline
              rows={4}
              value={content}
              onChange={(e) => setContent(e.target.value)}
            />
          </Paper>
          <Button
            variant="contained"
            color="tertiary"
            onClick={handleChatClick}
          >
            Chat
          </Button>
        </Box>
        <Box
          sx={{
            width: "370px",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
            gap: 2,
          }}
        >
          <Paper>
            <TextField
              label="Response by AI"
              color="tertiary"
              fullWidth
              multiline
              rows={4}
              value={gptAnswer}
              onChange={(e) => setGptAnswer(e.target.value)}
            />
          </Paper>
          <Button
            variant="contained"
            color="tertiary"
            onClick={handlePharaphaseClick}
          >
            Paraphrase
          </Button>
        </Box>
        <Box
          sx={{
            width: "270px",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
            gap: 2,
          }}
        >
        <Paper sx={{width:"365px"}}>
        <TextField
              label="Paraphrased Response"
              color="tertiary"
              fullWidth
              multiline
              rows={4}
              value={paraphrasedAnswer}
            />     
        </Paper>
        <Button
            sx={{width:"365px"}}
            variant="contained"
            color="tertiary"
            onClick={handlehandwrittenClick}
          >
            Download Handwritten
          </Button>

        </Box>
      </Container>
    </Box>
  );
}

export default Chat;
