import { ja } from "date-fns/locale/ja";
import DatePicker, { registerLocale } from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

// CSS Modules, react-datepicker-cssmodules.css
// import 'react-datepicker/dist/react-datepicker-cssmodules.css';

registerLocale("ja", ja);

interface DatePickerDialProps {
  selectedDate?: Date | null;
  setSelectDate?: (date: Date) => void;
}

const DatePickerDial: React.FC<DatePickerDialProps> = ({
  selectedDate,
  setSelectDate,
}) => {
  return (
    <DatePicker
      showIcon
      selected={selectedDate}
      onChange={(date) => setSelectDate?.(date ?? new Date())}
      locale={ja}
    />
  );
};

export default DatePickerDial;
