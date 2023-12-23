export function formatDate(dateString: string, options?: Intl.DateTimeFormatOptions | undefined): string{
  if(!options) options = { year: 'numeric', month: 'long', day: 'numeric' };
  return (new Date(dateString)).toLocaleDateString(undefined, options);
}

export function formatTime(dateString: string, options?: Intl.DateTimeFormatOptions | undefined): string{
  if(!options) options = { hour: 'numeric', minute: 'numeric' };
  return (new Date(dateString)).toLocaleTimeString(undefined, options);
}
