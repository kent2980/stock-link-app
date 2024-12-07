import React from "react";

const EditContents: React.FC = () => {
  return (
    <div>
      <h1>Edit Contents</h1>
      <form>
        <div>
          <label htmlFor="title">Title:</label>
          <input type="text" id="title" name="title" />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <textarea id="description" name="description"></textarea>
        </div>
        <button type="submit">Save</button>
      </form>
    </div>
  );
};

export default EditContents;
