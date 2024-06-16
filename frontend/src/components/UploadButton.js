import React, { useRef } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Button from "@mui/material/Button";
import { Typography } from "@mui/material";

function UploadButton({ icon, onFileSelect }) {
  const fileInputRef = useRef();

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    console.log(file);

    // Update the file state using onFileSelect callback
    if (onFileSelect) {
      onFileSelect(file);
    }
  };

  return (
    <>
      <Button
        variant="contained"
        color="tertiary"
        sx={{
          color:'#fff',
          p: "40px",
          width:"758px",
          fontSize: "1.5rem",
        }}
        onClick={handleButtonClick}
      >
        <FontAwesomeIcon icon={icon} style={{ marginRight: "10px", fontSize: '2em', color:'#fff'}} />
        <Typography sx={{fontWeight:500}}>Upload File</Typography> 
      </Button>
      <input
        type="file"
        style={{ display: "none" }}
        ref={fileInputRef}
        onChange={handleFileChange}
        accept="/*"
      />
    </>
  );
}

export default UploadButton;
