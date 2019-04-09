const dayOfWeek = ['일', '월', '화', '수', '목', '금', '토'];

function getDayOfWeek(date) {
  return dayOfWeek[date.getDay()];
}


export { getDayOfWeek };
