const dayOfWeek = ['일', '월', '화', '수', '목', '금', '토'];

function getDayOfWeek(date) {
  return dayOfWeek[date.getDay()];
}

function getDayString(date) {
  const tzoffset = (new Date()).getTimezoneOffset() * 60000;
  return new Date(date.getTime() - tzoffset).toISOString().split('T')[0];
}



export { getDayOfWeek, getDayString };
