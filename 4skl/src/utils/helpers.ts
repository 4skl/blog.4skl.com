export function formatDate(date: Date, options?: Intl.DateTimeFormatOptions | undefined): string{
  if(!options) options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(date).toLocaleDateString(undefined, options);
}

export function formatTime(date: Date, options?: Intl.DateTimeFormatOptions | undefined): string{
  if(!options) options = { hour: 'numeric', minute: 'numeric' };
  return new Date(date).toLocaleTimeString(undefined, options);
}
