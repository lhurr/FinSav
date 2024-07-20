import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { useEffect, useRef, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import Plot from 'react-plotly.js';
import {
  useChatInteract,
  useChatMessages,
  IStep,
  useChatData,
} from "@chainlit/react-client";

export function Playground() {
  const [inputValue, setInputValue] = useState("");
  const { sendMessage } = useChatInteract();
  const { messages } = useChatMessages();
  const { elements } = useChatData();
  const [fetchedData, setFetchedData] = useState<Record<string, any>>({});

  const messagesEndRef = useRef<any>(null);

  const handleSendMessage = () => {
    const content = inputValue.trim();
    if (content) {
      const message = {
        name: "You",
        type: "user_message" as const,
        output: content,
      };
      sendMessage(message, []);
      setInputValue("");
    }
  };

  useEffect(() => {
    scrollToBottom();
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages, elements]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    const fetchData = async () => {
      const dataPromises = elements
        .filter((element) => element.mime === 'application/json')
        .map(async (element) => {
          try {
            const res = await fetch(element.url as string);
            if (!res.ok) {
              throw new Error(`Failed to fetch data from ${element.url}`);
            }
            const data = await res.json();
            return { url: element.url, data };
          } catch (error) {
            console.log('An error occured!');
            return { url: element.url, data: null };
          }
        });

      const fetchedDataArray = await Promise.all(dataPromises);
      const dataObject = fetchedDataArray.reduce((acc, curr) => {
        acc[curr.url as string] = curr.data;
        return acc;
      }, {} as Record<string, any>);

      setFetchedData(dataObject);
    };

    fetchData();
  }, [elements]);

  const renderMessage = (message: IStep) => {
    const dateOptions: Intl.DateTimeFormatOptions = {
      hour: "2-digit",
      minute: "2-digit",
    };
    const date = new Date(message.createdAt).toLocaleTimeString(
      undefined,
      dateOptions
    );

    return (
      <div key={message.id} className="flex items-start space-x-2 mt-20">
        {message.name === 'FinSav' ? (
          <div><img src="/img.png" className="rounded-full" alt="" /></div>
        ) : (
          <div className="text-sm text-black-500 font-semibold">{message.name}</div>
        )}
        <div className="flex-1 border rounded-lg p-2">
          <ReactMarkdown remarkPlugins={[remarkGfm]} className="text-black dark:text-white">
            {message.output}
          </ReactMarkdown>
          {elements.filter((e) => e.forId === message.id).map((image) => (
            image.mime === 'application/json' 
            ? fetchedData[image.url as string] && <div ><Plot data={fetchedData[image.url as string]?.data} layout={fetchedData[image.url as string]?.layout} /></div>
            : <div key={image.url}><img src={image.url} width={600} className="img-fluid border-solid border-2 border-sky-700 rounded mt-2" alt="Plot" /></div>
          ))}
          <small className="text-xs text-gray-500">{date}</small>
        </div>
      </div>
    );
  };

  return (
    <div className="flex-1 overflow-hidden bg-gray-50 dark:bg-gray-900 flex flex-col">
      <div className="flex-1 overflow-auto p-6 space-y-4">
        {messages.map((message: any) => renderMessage(message))}
        <div ref={messagesEndRef} /> {/* Ref to the last message */}
      </div>
      <div className="border-t p-4 bg-white dark:bg-gray-800">
        <div className="flex items-center space-x-2">
          <Input
            autoFocus
            className="flex-1"
            id="message-input"
            placeholder="Type a message"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyUp={(e) => {
              if (e.key === "Enter") {
                handleSendMessage();
              }
            }}
          />
          <Button onClick={handleSendMessage} type="submit">
            Send
          </Button>
        </div>
      </div>
    </div>
  );
}
