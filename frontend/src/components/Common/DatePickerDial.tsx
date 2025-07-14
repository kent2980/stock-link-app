import { useState } from "react";
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";

// CSS Modules, react-datepicker-cssmodules.css
// import 'react-datepicker/dist/react-datepicker-cssmodules.css';

const DatePickerDial = () => {
  const [selectedDate, setSelectedDate] = useState<Date | null>(new Date());
  return (
    <DatePicker
      showIcon
      selected={selectedDate}
      onChange={(date) => setSelectedDate(date)}
    />
  );
};

export default DatePickerDial;
