import React, { useState, useEffect} from "react";

const url = "http://localhost:8000";

interface Table {
  Id: number,
  IpAddres: string,
  RequestURL: string,
  RequestPort: string,
  RequestPath: string,
  RequestMethod: string,
  RequestTime: string,
  BrowserType: string,
  ServiceName: string,
}

const Table: React.FC = () => {
    const [data, setData] = useState<Table[]>([]);
    

    useEffect(() => {
      fetch(url)  
        .then(res => res.json())
        .then(data => setData(data));
    }, []);


    return (
        <div>
          <h1>Logs</h1>
          <table>
            <tr>
              <th>IP Address</th>
              <th>Request URL</th>
              <th>Request Port</th>
              <th>Request Path</th>
              <th>Request Method</th>
              <th>Request Time</th>
              <th>Browser Type</th>
              <th>Service Name</th>
            </tr>


            {data.map(item => (
              <tr key={item.Id}>

                <td>{item.IpAddres}</td>     
                <td>{item.RequestURL}</td>        
                <td>{item.RequestPort}</td>  
                <td>{item.RequestPath}</td>
                <td>{item.RequestMethod}</td>
                <td>{item.RequestTime}</td>
                <td>{item.BrowserType}</td>  
                <td>{item.ServiceName}</td> 
                  
              </tr>
            ))}

          </table>

        </div>

      );

};
