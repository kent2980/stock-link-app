import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";

// CSS Modules, react-datepicker-cssmodules.css
// import 'react-datepicker/dist/react-datepicker-cssmodules.css';

interface DatePickerDialProps {
  selectedDate?: Date | null;
  setSelectDate?: (date: Date | null) => void;
}

const DatePickerDial: React.FC<DatePickerDialProps> = ({
  selectedDate,
  setSelectDate,
}) => {
  return (
    <DatePicker
      showIcon
      selected={selectedDate}
      onChange={(date) => setSelectDate?.(date)}
      locale="ja"
    />
  );
};

export default DatePickerDial;
