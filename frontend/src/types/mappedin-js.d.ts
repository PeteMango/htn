declare module '@mappedin/mappedin-js' {
    export class Platform {
      constructor(config: { apiKey: string; apiSecret: string });
      getVenue(mapId: string): Promise<any>;
    }
    export function show3dMap(container: HTMLElement, mapData: any): Promise<any>;
  }